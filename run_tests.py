import glob
import os
import re
import shutil

def add_screenshots(test_path, indentation="\t"):
    """
    Add cy.screenshot command after each cy.visit in a manually recorded Cypress test scenario

    Parameters:
    test_path (str): relative path of a test (Cypress test file)
    indentation (str): indentation type

    Returns:
    This function does not return anything. It writes the new test in the baseline directory.
    """

    new_test = []
    test_name = os.path.basename(test_path) 

    with open(test_path) as f:
        lines = f.readlines()

        screenshot_counter = 0
        for line in lines:
            new_test.append(line)
            if "cy.visit" in line:
                new_test.append("{}cy.matchScreenshot('{}_{}')".format(indentation, test_name, screenshot_counter))
                screenshot_counter += 1

    baseline_test_path = os.path.join("cypress/integration/baseline", test_name)

    with open(baseline_test_path, "w") as f:
        for line in new_test:
            f.write(line)
    

def change_domain(test_path, baseline_url, migration_url):
    """
    Replace baseline url by migration url in a Cypress test file

    Parameters:
    test_path (str): relative path of a test (Cypress test file)
    baseline_url (str) 
    migratio_url (str) 

    Returns:
    This function does not return anything. It writes the new test in the baseline directory.
    """


    with open(test_path) as f:
        content = f.read()
        new_content = content.replace(baseline_url, migration_url)

    test_name = os.path.basename(test_path) 
    migration_test_path = os.path.join("cypress/integration/migration", test_name)

    with open(migration_test_path, "w") as f:
        f.write(new_content)
    


if __name__ == "__main__":
    baseline_url = "http://coalescent.brandonsavage.net/"
    migration_url = "https://migration.coalescent-inc.com/"

    # Clear generated tests, videos and screenshots
    os.system("rm -rf cypress/match-screenshots/*")
    os.system("rm -rf cypress/videos")
    os.system("rm -rf cypress/integration/baseline/*.js")
    os.system("rm -rf cypress/integration/migration/*.js")

    # Baseline tests
    # Copy recorded tests and add screenshot commands after each cy.visit() 
    recorded_test_paths = glob.glob("cypress/integration/recorded/*.js") 
    for recorded_test_path in recorded_test_paths:
        add_screenshots(recorded_test_path)

    # Migration tests
    # Change domain name and copy tests in migration directory
    baseline_test_paths = glob.glob("cypress/integration/baseline/*.js") 
    for baseline_test_path in baseline_test_paths:
        change_domain(baseline_test_path, baseline_url, migration_url)

    # Run Cypress tests
    record_video = False
    os.system('npx cypress run --spec "cypress/integration/baseline/*.js"')
    os.system('npx cypress run --spec "cypress/integration/migration/*.js"')