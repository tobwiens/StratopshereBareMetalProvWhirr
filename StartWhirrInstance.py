'''
Created on 25/03/2014

@author: Tobias Wiens
'''

MAXIMUM_TRIES = 100

from WhirrProvisioningInstance import WhirrConfigFileManager, BotoConnectionManager, AmazonSSHUtils
import sys


def getFileContent(fileWithPath):
    '''
    Tries to get the key material from hard disk or creates another keyPair and saves it on hard disk
    @param keyName: Name of the key in amazon ec2
    @type keyName: String
    @param keyPath: Local path and file name of the key /path/to/key/file.pem for example
    @type keyPath: String
    '''
    print fileWithPath
    openKeyFile = file(fileWithPath, 'r')
    #create empty string and concatinate lines
    result = ''
    for line in openKeyFile:
        result += line
        
    openKeyFile.close()
    return result 
    

if __name__ == '__main__':
    print 'Stratosphere EC2 Deployment'
    
    #To connect to amazon we need to read the region which to connect to, out of the config file
    configFile = WhirrConfigFileManager.ConfigFileManager()
    print 'Config file opened'
    
    #Connect to amazon region
    amazonConnection = BotoConnectionManager.BotoConnectionManager(aws_secret_key=configFile.getAWSAccesKey(), aws_key_id=configFile.getAWSKeyID(), region=configFile.getRegion())
    print "Successfully connected to region "+configFile.getRegion()
    
    #authorizeSSH access - Whirr instance
    if AmazonSSHUtils.authorizeSSH(securityGroupName = configFile.getSecurityGroup(), amazonConnection = amazonConnection, ipAddress=configFile.getIPAccess()) is False:
        print 'Security group '+configFile.getSecurityGroup()+' not found'
        sys.exit('Update config file')
    
    #Get secret SSH key
    keyMaterial = getFileContent(fileWithPath=configFile.getKeyPath())
    
    #Get user data
    userData = "#!/bin/bash -x \n exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1 \n"
    #add user name
    userData += 'loginUser='+configFile.getUsername()+'\n'
    userData += 'javaPath='+configFile.getJavaHome()+'\n'
    userData += 'homePath=/home/$loginUser \n'
    userData += 'whirrPath=$homePath/whirr-0.8.2\n'
    userData += 'echo "'+keyMaterial+'"  >> $homePath/.ssh/whirr_id_rsa \n'
    userData += 'chmod 600 $homePath/.ssh/whirr_id_rsa \n'
    userData += 'ssh-keygen -y -f $homePath/.ssh/whirr_id_rsa >> $homePath/.ssh/whirr_id_rsa.pub \n'
    userData += getFileContent(fileWithPath=configFile.getUserDataFile())

    print 'Start one instance of type '+configFile.getInstanceType()+' to run the provisioning instance with image id: '+configFile.getImageId()
    whirrInstanceReservation = amazonConnection.ec2RegionConnection.run_instances(image_id=configFile.getImageId(),instance_type=configFile.getInstanceType(), key_name=configFile.getKeyName(), security_groups=[configFile.getSecurityGroup()], user_data=userData, dry_run=False)
    

    