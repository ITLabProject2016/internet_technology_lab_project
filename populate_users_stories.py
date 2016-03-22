import stories.populate_zombies_story1
import stories.populate_zombies_story2
import stories.populate_zombies_story3
import stories.populate_zombies_story4
import stories.populate_users

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    default = '\033[0m'

if __name__ == '__main__':
    print bcolors.WARNING + "Populating story 1..."
    stories.populate_zombies_story1.populate()
    print bcolors.OKBLUE + "Populating story 2..."
    stories.populate_zombies_story2.populate()
    print bcolors.OKGREEN + "Populating story 3..."
    stories.populate_zombies_story3.populate()
    print bcolors.HEADER + "Populating story 4..."
    stories.populate_zombies_story4.populate()
    print bcolors.OKGREEN + "Populating users..." + bcolors.default
    stories.populate_users.populate()
