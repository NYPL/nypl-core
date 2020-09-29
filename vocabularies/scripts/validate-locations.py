from deepdiff import DeepDiff
from git import Git
import json

# Provides a comparison on the serialized Locations JSON-LD object in the
# current working branch
def main():
    # Initialize git client and store current branch name
    git = Git()
    currentBranch = None
    for branch in git.branch().split('\n'):
        if branch[0] == '*':
            currentBranch = branch[2:]
            break

    # Get current working copy of the locations JSON-LD file
    newLocationFile = openLocationsJsonFile()

    # Checkout master and get the current version
    git.checkout('master')
    masterLocationFile = openLocationsJsonFile()

    # Compare the two objects
    newKeys = []
    deletedKeys = []
    alteredKeys = []
    newLocDict = {item['skos:notation']: item for item in newLocationFile['@graph']}
    masterLocDict = {item['skos:notation']: item for item in masterLocationFile['@graph']}

    for key, item in newLocDict.items():
        if key not in masterLocDict.keys():
            newKeys.append(key)
        else:
            diff = DeepDiff(newLocDict[key], masterLocDict[key], ignore_order=True)
            if len(diff.keys()) > 0:
                alteredKeys.append((key, diff))
    
    for key in masterLocDict.keys():
        if key not in newLocDict.keys():
            deletedKeys.append(key)


    # Output comparison results
    print('Keys Added: {}'.format(len(newKeys)))
    print('Keys Deleted: {}'.format(len(deletedKeys)))
    print('Keys Altered: {}'.format(len(alteredKeys)))
    displayAlterations(alteredKeys) # Provide details on altered mapping objects

    # Reset to current working branch
    git.checkout(currentBranch)


def openLocationsJsonFile():
    with open('./../json-ld/locations.json') as locFile:
        return json.load(locFile)


def displayAlterations(alteredKeys):
    for key, diff in alteredKeys:
        print('\nALTERED KEY: {}'.format(key))
        for change in ['type_changes', 'values_changed']:
            if change in diff.keys():
                for label, changes in diff[change].items():
                    print('Attribute: {}'.format(label))
                    print('Old Value: {}'.format(changes['old_value']))
                    print('New Value: {}'.format(changes['new_value']))
        
        if 'iterable_item_removed' in diff.keys():
            for label, removal in diff['iterable_item_removed'].items():
                print('Attribute(Pos): {}'.format(label))
                print('Removed Value: {}'.format(removal))
        
        if 'iterable_item_added' in diff.keys():
            for label, addition in diff['iterable_item_added'].items():
                print('Attribute(Pos): {}'.format(label))
                print('Added Value: {}'.format(addition))


if __name__ == '__main__':
    main()
