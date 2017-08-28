#Classes and methods for working with files and folders
import os  #For works with dirs and other system
import subprocess  #For call in terminal
import shutil  #For work with files and folders
import logging #For write logs

SEP = os.sep  #Symbol of separation (/ in Linux; \ in Windows)

class Basic:  #Basic functions for work with files/folders
    def path_to(self, name):
        '''Path to "name" in this directory'''
        path_to = os.getcwd() + SEP + name
        return path_to
    def path_to_FiF(self, folder, file):
        """Path to 'file' in folder 'folder'"""
        folder_ = Basic.path_to(self, folder)
        path = folder_ + SEP + file
        return path
    def r_acces(self, name, mode='a+rwx'):
        """Change acces on file or folder"""
        logging.info('Changing acces for ' + name + '...')
        commands = 'sudo chmod ' + mode + '' + '\'' + os.getcwd() + SEP + name + '\''
        subprocess.Popen(commands, shell=True)
        logging.debug('Sucefly Changing acces for ' + name + '!')
    def move(self, of, to):
        """The same if shutil.move, but with exceptions"""
        try:
            logging.info('Trying move file/folder ' + of + ' in ' + to + '...')
            shutil.move(of, to)
        except shutil.Error:
            logging.critical('Can\'t move file/folder ' + of + ' in ' + to + '!')
        logging.debug('Sucefly move file/folder ' + of + ' in ' + to + '!')



class Files: #Methods for working with files
    def n_file(self, name, path=None):
        '''Make new file in this dir or in "path"'''
        try:
            logging.info('Making file ' + name + '...')
            new = open(name, 'x')
            logging.debug('Sucefly make file ' + name + '!')
            logging.info('Changing acces for ' + name + '...')
            Basic.r_acces(self, name)
            logging.debug('Sucefly Changing acces for ' + name + '!')
            if path == None:
                pass
            else:
                logging.info('Moving file ' + name + ' in ' + path + '...')
                name = Basic.path_to(self, name)
                path = Basic.path_to(path)
                Basic.move(self, name, path)
                logging.debug('Sucefly move file ' + name + ' in ' + path + '!')
            new.close()
        except FileExistsError:
            logging.debug('File ' + name + ' is exist!')


class Folders(Basic): #Methods for working with dirs
    def rem_fold(self, name):
        '''This method remove folder what writed in "name" '''
        path = Basic.path_to(self, name)  #Full path to folder
        try:
            logging.info('Trying remove ' + name + '...')
            os.rmdir(path)  #Remove the folder
            logging.debug('Sucefly remove' + name + '!')
        except FileNotFoundError:
            logging.critical('File ' + name + ' not found.')
        except OSError:
            logging.debug('Directory' + name + 'is not empty...')
            shutil.rmtree(name)
            logging.debug('Sucefly remove' + name + '!')
    def n_fold(self, name):
        """This method create a new folder"""
        way_to_fold = os.getcwd()
        if os.path.isdir(name) != True:  #If the folder "name" not exist
            logging.info('Making folder ' + name + '...')
            os.mkdir(name)
            logging.info('Changing acces for ' + name + '...')
            Basic.r_acces(self, name)
            logging.debug('Sucefly change acces for ' + name + '!')
        else:
            logging.warning('Folder ' + name + ' is exist')


def main():
	folders = Folders()
	files = Files()
	basic= Basic()


if __name__ == "__main__":
    main()
