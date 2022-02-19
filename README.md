[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/steinkohl/quote-service/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python Lint and Static Analysis](https://github.com/steinkohl/quote-service/actions/workflows/lint.yaml/badge.svg)](https://github.com/steinkohl/quote-service/actions/workflows/lint.yaml)
[![Python Testing](https://github.com/steinkohl/quote-service/actions/workflows/testing.yaml/badge.svg)](https://github.com/steinkohl/quote-service/actions/workflows/testing.yaml)
[![Docker Build and Upload](https://github.com/steinkohl/quote-service/actions/workflows/dockerhub.yml/badge.svg)](https://github.com/steinkohl/quote-service/actions/workflows/dockerhub.yml)


# quote-service

The quote-service is a microservice which serves quotes via gRPC API.

The docker image is build automatically after every change in the main branch and pushed to [Docker Hub](https://hub.docker.com/r/csecsecse/quote-service).

To pull the image from docker hub, you just have to execute the command:

``
docker pull csecsecse/quote-service
``

The default port for gRPC is set to 50055, the protobuffer can be compiled with the [proto file](./proto/quote.proto).

A guide how to compile the proto buffer: [Google's Protocol Buffer Guide](https://developers.google.com/protocol-buffers/docs/overview)



## License
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/steinkohl/quote-service/blob/main/LICENSE)

This project is licensed under the MIT License. Please see the <a href="./LICENSE">LICENSE</a> file in the root directory for more information on the license.
