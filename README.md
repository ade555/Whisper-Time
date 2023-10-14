# WhisperTime (WIP)

<!-- <p>
   <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat" alt=""></a>
   <a href="https://golang.org"><img src="https://img.shields.io/badge/Made%20with-Go-1f425f.svg" alt="made-with-Go"></a>
   <a href="https://goreportcard.com/report/github.com/goodnessuc/paywalletengine"><img src="https://goreportcard.com/badge/github.com/goodnessuc/paywalletengine" alt="GoReportCard"></a>
   <a href="https://github.com/goodnessuc/paywalletengine"><img src="https://img.shields.io/github/go-mod/go-version/goodnessuc/paywalletengine.svg" alt="Go.mod version"></a>
   <a href="https://github.com/goodnessuc/paywalletengine/blob/master/LICENSE"><img src="https://img.shields.io/github/license/goodnessuc/paywalletengine.svg" alt="LICENSE"></a>
</p> -->


## Introduction

WhisperTime is an MVP API for chat applications created with Django Rest Framework and Redis. Some of its features include email authentication, user management and real-time messaging. With WhisperTime, developers can easily integrate secure and efficient chat functionality into their applications without having to build everything from scratch.

In addition to basic chat functionality, WhisperTime offers real-time messaging, allowing users to send and receive messages instantly. The API leverages Redis, a high-performance in-memory data store, to enable lightning-fast message delivery and ensure a seamless chat experience even under high loads.

## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#Installation-and-Setup)
- [Testing](#testing)
- [API Documentation](docs/readme.md)
- [Databases](docs/databases.md)
- [Technologies and Tools](#technologies-and-tools)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

The following instructions will help you install WhisperTime on your local system and have it running.

### Prerequisites

- Python 3.10 or higher

### Installation and Setup

1. Clone the repository

```
git clone https://github.com/ade555/WhisperTime.git
```

2. Change directory to the project folder

```
cd WhisperTime
```

3. Create a virtual environment
```
python -m venv env
```

4. Install the project dependencies into your virtual environment

```
pip install -r requirements.txt
```

5. Generate a new secret key

```
python secret_key.py
```

6. Create an environment variable (`.env` file) and include the necessary information from the `.env_sample` file

7. Open your CLI and start the project

```
python manage.py runserer
```

## Testing

## Technologies and Tools

- [Python](https://www.python.org/) - The programming language used
- [JWT](https://jwt.io/) - JSON Web Tokens for authentication

## Contributing

Contributions are welcome! Feel free to open a pull request right away.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
