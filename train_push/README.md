![](https://img.shields.io/badge/python-3.6-yellow)

A image that will train a classifer and push the model on GitHub repo

This is based on centos:latest image. This image will make a random forest classifier model, using sci-kit learn module and push it to the repository specfied.

Click here to see Docker Hub repo 🐳 --> [Link](https://hub.docker.com/repository/docker/yashindane/random-forest-trainer/general)

Have a GitHub repo initialized with any name, where the model will be pushed

It uses environment variables, export them by -

`export variable-name`

To run the container-

`docker run -it -e RANDOM_STATE=value -e TEST_SIZE=value -e TREES=value -e CRITERIA=value -e GIT_USRN=value
-e GIT_REPON=value --name container-name yashindane/random-forest-trainer:tagname`

| env variable | description |
| ------------ | ----------- |
| RANDOM_STATE | Controls both the randomness of the bootstrapping of the samples |
| TEST_SIZE    | the percentage of test values (between 0 to 1) |
| TREES        | no. of trees to use in model |
| CRITERIA     | The function to measure the quality of a split (entropy, mse, mae etc) |
| GIT_USRN     | Your GitHub username |
| GIT_REPON    | repo name |

Once the container starts, it is required to upload your dataset (should be named as train.csv)

For uploading dataset -

`docker cp <path-for-train.csv> :/ml_folder`

Enter your credentials when prompted.



