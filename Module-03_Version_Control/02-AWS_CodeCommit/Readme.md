# AWS CodeCommit

## 01. What is AWS CodeCommit?

- AWS CodeCommit is a version control service hosted by Amazon Web Services.
- You can use it to privately store and manage application assets (such as documents, source code, and binary files) in the cloud.
- CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories.
- It eliminates the need for you to manage your own source control system or worry about scaling its infrastructure.
- You can use CodeCommit to store anything from code to binaries.
- It supports the standard functionality of Git, so it works seamlessly with your existing Git-based tools.

## 02. Why AWS CodeCommit?

- Fully Managed Service
- Source Code Security
- Built-in Scalability
- Collaboration with Code
- Integrations with other AWS services
- Easy Migration from any other Git repo to CodeCommit

## 03. How to use AWS CodeCommit?

There are multiple ways to use AWS CodeCommit:

- **AWS Management Console**
  - Sign-in to your AWS Account from management console: https://console.aws.amazon.com/.
  - Navigate to **CodeCommit** service
- **Git Commands**
  - Use the standard Git commands to manage your code.
- **AWS CLI Commands**
  - Use the AWS CLI commands to manage your code, branches, and pull requests.

## 04. Getting started with AWS CodeCommit

### Step-01: Create a CodeCommit repository

- Open the CodeCommit console >> Click **Create Repository** button
- On the Create repository page, in Repository name, enter a name for your repository (for example, binAppRepos).
- (Optional) In Description, enter a description (for example, This repos has app code). This can help you and other users identify the purpose of the repository.
- Click **Create** button

### Step-02: Add files to your repository (commit)

You can add files to your repository by following ways:

1. **From CodeCommit console**
   - If you create the first file for a repository in the console, a branch is created for you with a name **main**.
   - This branch is the _default branch_ for your repository.
2. **Uploading a file from your local computer using the CodeCommit console**

3. **Using a Git client**

   - First, clone the repository to your local computer

   ```
   git clone <your_github_repo_url>
   ```

   - Then add the committing, and pushing files to the CodeCommit repository.

   ```
   git add .

   git commit -m <commit_message>

   git push -u <origin> <remote_branch>
   ```

### Step-03: Browse the contents of your repository

- Navigate to the AWS CodeCommit service dashboard >> Repositories
- Select your repository from the list. It will display the contents present in the default branch of your repository.

### Step-04: Collaborate with Pull Request

- You can create a pull request so that other users can review and comment on your code changes in a branch.
- You can also create one or more approval rules for the pull request.
- In the navigation pane, choose **Pull requests** >> **Create pull request**
- In Create pull request, in _Source_, choose the branch that contains the changes you want reviewed. In _Destination_, choose the branch where you want the reviewed code to be merged when the pull request is closed. Choose Compare.
