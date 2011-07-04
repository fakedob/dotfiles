if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

if [ -f /opt/local/etc/bash_completion ]; then
    . /opt/local/etc/bash_completion

    source ~/.bash/completion/git-completion.bash
fi


##
# Your previous /Users/mignev/.bash_profile file was backed up as /Users/mignev/.bash_profile.macports-saved_2011-06-18_at_01:30:11
##

# MacPorts Installer addition on 2011-06-18_at_01:30:11: adding an appropriate PATH variable for use with MacPorts.
export PATH=/opt/local/bin:/opt/local/sbin:$PATH
# Finished adapting your PATH environment variable for use with MacPorts.

export PATH=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/:$PATH
