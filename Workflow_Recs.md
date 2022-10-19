# Suggested Workflow Methodology

### Purpose: Avoid and Prevent Merge Conflicts
- These are inevitable, but hopefully, we can minimize them.

1. From main branch, get latest version to be up to date
    - `git fetch`
    - `git pull`
2. Checkout a new branch to work on a feature
    - This will enable that new branch has most up to date changes with `main`
    - `git checkout -b <name/single-feature>`
3. Work on feature
    - test and make sure it works
    - prior to merge, sync for group code review
4. Merge Branch
    - I do this in github cause it is easy
    - this will automatically delete branch
