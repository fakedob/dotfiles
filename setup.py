#/usr/bin/env python
from sys import argv
from os import listdir, getenv, getcwd, path, mkdir, system

home_dir = getenv('HOME')
current_dir = getcwd()
current_user = getenv('USER')

oldfiles_backup_dir = home_dir + '/' + current_user + '_old_dotfiles_backup'

excludes = ['README', 'setup.py', '.gitignore', '.git', '.gitmodules']
backup_files = ['.bashrc', '.vim', '.vimrc', '.bash_profile', '.gitconfig', '.profile', '.tmux.conf', 'python', 'virtualenvs', '.gitignore', '.inputrc']

files = listdir( current_dir )

def main():
    try:
        action = argv[1]
    except IndexError:
        action = 'install'

    if action == 'install':
        make_backup()

    install_dotfiles()

def make_backup():
    if not path.exists(oldfiles_backup_dir):
        mkdir(oldfiles_backup_dir)

    for file in listdir( home_dir ):
        the_file = home_dir + '/' + file 
        
        if file in backup_files:
            system("cp -R "+ the_file + " " + oldfiles_backup_dir + "/")

def install_dotfiles():    
    virtenvsdir = current_dir + '/virtualenvs'
    if not path.exists( virtenvsdir ):
        mkdir( virtenvsdir )
        system('ln -s ' + virtenvsdir + ' ' + home_dir + '/.virtualenvs')

    for file in files:
        if file not in excludes:
            the_home_file = home_dir + '/.' + file
            the_file = current_dir + '/' + file

            system('rm -rf ' + the_home_file)
            system('ln -s ' + the_file + ' ' + the_home_file)

if __name__ == '__main__':
    main()
