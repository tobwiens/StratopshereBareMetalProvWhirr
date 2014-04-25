'''
Created on 25/03/2014

@author: Tobias Wiens
'''
import ConfigParser

class ConfigFileManager(object):
    '''
    This file is managing the config file which inherits all important configuration variables.
    The config file contains an overall section which contains:
    aws_key_id
    aws_acces_key
    region
    image id
    setup commands
    create setup image id with name
    '''

    #Global variables
    configPath = 'conf/instances.cfg'
    config = None
    
    #Section names
    OVERALL_SECTION_NAME = 'Basic'
    INSTANCE_SECTION_NAME = 'Instance'
    JAVA_SECTION_NAME = 'Java'
    STRATOSPHERE_SECTION_NAME = 'Stratosphere'
    
    #Overall section OPTIONS
    OVERALL_AWS_SECRET_KEY = 'aws-secret-key'
    OVERALL_AWS_KEY_ID = 'key-ID'
    OVERALL_KEY_PATH = 'key-path'
    OVERALL_KEY_NAME = 'key-name'
    OVERALL_REGION = 'region'
    OVERALL_IPACCES = 'IP-access'
    
    
    INSTANCE_IMAGE_ID = 'image-ID'
    INSTANCE_USERNAME = 'username'
    INSTANCE_INSTANCE_TYPE = 'instance-type'
    INSTANCE_SECURITY_GROUP = 'security-group'
    INSTANCE_INSTANCE_COUNT = 'instance-count'
    INSTANCE_USER_DATA_FILE = 'user-data-file'    
    
    JAVA_JAVA_HOME = 'java-home-directory'
    
    
    
    
    
    def __init__(self, configPath=None):
        '''
        Constructor:
        Create config file. If file does not exist a new empty configuraion file will be created
        @param configPath: /path/to/file/file.config
        @type configPath: String
        '''
        if configPath is not None:
            self.configPath = configPath
        
        #create config object
        self.config = ConfigParser.ConfigParser()
        try:
            openConfigFile = file(self.configPath, "r")
            self.config.readfp(fp=openConfigFile)
        except IOError as e:
            print e
            print 'No config file found '+configPath  
         
       
    
        
    def getAWSAccesKey(self):
        return self.config.get(section=self.OVERALL_SECTION_NAME, option=self.OVERALL_AWS_SECRET_KEY)
    
    def getAWSKeyID(self):
        return self.config.get(section=self.OVERALL_SECTION_NAME, option=self.OVERALL_AWS_KEY_ID)
    
    def getImageId(self):
        return self.config.get(section=self.INSTANCE_SECTION_NAME, option=self.INSTANCE_IMAGE_ID)
    
    def getRegion(self):
        return self.config.get(section=self.OVERALL_SECTION_NAME, option=self.OVERALL_REGION)
    
    def getIPAccess(self):
        return self.config.get(section=self.OVERALL_SECTION_NAME, option=self.OVERALL_IPACCES)
    
    def getUsername(self):
        return self.config.get(section=self.INSTANCE_SECTION_NAME, option=self.INSTANCE_USERNAME)
    
    def getKeyPath(self):
        return self.config.get(section=self.OVERALL_SECTION_NAME, option=self.OVERALL_KEY_PATH)
    
    def getKeyName(self):
        return self.config.get(section=self.OVERALL_SECTION_NAME, option=self.OVERALL_KEY_NAME)
    
    def getInstanceType(self):
        return self.config.get(section=self.INSTANCE_SECTION_NAME, option=self.INSTANCE_INSTANCE_TYPE)
   
    def getSecurityGroup(self):
        return self.config.get(section=self.INSTANCE_SECTION_NAME, option=self.INSTANCE_SECURITY_GROUP)
    
    def getInstanceCount(self):
        return self.config.get(section=self.INSTANCE_SECTION_NAME, option=self.INSTANCE_INSTANCE_COUNT)
    
    def getUserDataFile(self):
        return self.config.get(section=self.INSTANCE_SECTION_NAME, option=self.INSTANCE_USER_DATA_FILE)
    
    def getJavaHome(self):
        return self.config.get(section=self.JAVA_SECTION_NAME, option=self.JAVA_JAVA_HOME)
    