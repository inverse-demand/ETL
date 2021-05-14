# ETL script using os cmd

import os

def etl(directory = '', file_name = '', new_upload = '', db_file_system = ''):
    if new_upload == True:
        cmd = """
        
        dbfs cp "{0}/{1}" dbfs:/{2}
        
        """.format(directory, file_name)
        
    elif new_upload == False:
        cmd = """
        
        dbfs cp "{0}/{1}" dbfs:/{2} --overwrite
        
        """.format(directory, file_name, db_file_system)
        
    else:
        raise Exception(
            """
            Please use a valid arguement, such as:
            
            directory = 'C:/Users/username/Documents'
            file_name = 'data.csv'
            new_upload = True #Use Boolean
            
            """
            )
        
    returned_value = os.system(cmd)
    print('returned value:', returned_value)

if __name__ == '__main__':
    etl(directory='', file_name='', new_upload='', db_file_system = '')
