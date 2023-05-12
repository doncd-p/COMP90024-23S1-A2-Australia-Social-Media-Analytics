# COMP90024-23S1-A2-Australia-Social-Media-Analytics
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue)

## Project Workflow

![workflow](/doc/images/workflow.jpg)
### Branches
The project follows a specific branching model to maintain a clean and organized repository:

1. `main`: The main branch represents the stable, production-ready version of the application. ***Note that it is not allowed to make direct commits to the `main` branch.***
2. `develop`: The develop branch is used for developing new features and bugfixes before they are merged into the `main` branch. It is checked out from the `main` branch, and ***Note that `develop` branch should not be merged into any other branch except for `test` branch.***
3. `test`: The test branch is used for testing by the QA. It is checked out from the  `develop`. After the testing is complete and the team has received feedback from the tester, they decide whether to create a release branch. ***Note that `test` branch should not be merged into other branch.***
4. `feature/<feature name>`: Feature branches are created for each new feature or enhancement, e.g., `feature/map` for the map feature. They should be checked out from the `develop` branch and merged back into it once the feature is complete.
5. `fix/<bug name>`: Bugfix branches are created for fixing bugs and issues, e.g., `fix/issue202`. They should be based on the  `develop` branch, but in some cases, they can be checked out from the `main` branch for emergency hotfix. Once the bug is fixed, the branch should be merged back into the respective base branch.
6. `release/<version number>`: Release branches are created for preparing new releases, e.g.,`release/v1.0.0`. They are checked out from the `develop` branch. After the release is complete and tested, the developer creates a pull request for the QA team to review. If approved, the release branch is merged into the `main` branch with a tag, and then deleted. Additionally, the release branch should be merged back into the `develop` branch to include any fixes or changes made during the release process.

### Naming Conventions
1. Branch names: Use lowercase letters and separate words with hyphens (e.g., feature/new-feature).
2. Commit messages: Write concise and descriptive commit messages, starting with a capital letter and using the imperative mood (e.g., 'Add new feature' or 'Fix bug in feature').
3. Style guid: 
    - Python: [Google python style guide](https://google.github.io/styleguide/pyguide.html)
    - Javascript: [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html
)

### Pull Requests and Code Review
1. When a feature or bugfix is complete, submit a pull request to the `develop` branch.
2. Request a code review from a team member.
3. Address any comments or requested changes.
4. After approval, merge the pull request into the `develop` branch and delete the feature or bugfix branch.