# Training Slack Chatbot

A production-ready Slack chatbot built with Python, AWS CDK, and containerized deployment workflows.

This project provides infrastructure-as-code, CI/CD integration, Kubernetes deployment manifests, and Dockerized runtime support for running a Slack bot in cloud environments.

---

## 📦 Project Structure

```
training-slack-chatbot/
│
├── .github/                 # GitHub workflows
├── cdk/                     # AWS CDK infrastructure code
├── lambdas/                 # Lambda handlers (if applicable)
├── lib/                     # Core chatbot logic
├── scripts/                 # Utility scripts
│
├── Dockerfile               # Runtime container definition
├── Dockerfile.cdk           # CDK container image
├── Jenkinsfile              # CI pipeline
├── Makefile                 # Project automation
│
├── KubernetesPods.yaml      # Kubernetes deployment
├── KubernetesPodsArm64.yaml # ARM64 deployment variant
├── msaas-config.yaml        # Environment/service configuration
│
├── requirements.dev.txt     # Development dependencies
├── README.md
├── GETTINGSTARTED.md
├── CONTRIBUTING.md
└── CHANGELOG.md
```

---

## 🚀 Overview

This chatbot supports:

- Slack Events API integration
- Container-based deployment
- Kubernetes orchestration
- AWS CDK infrastructure provisioning
- CI/CD via Jenkins
- Multi-architecture (x86 + ARM64) deployment

---

## 🛠 Development Setup

### 1. Clone Repository

```bash
git clone https://github.com/<your-org>/training-slack-chatbot.git
cd training-slack-chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.dev.txt
```

---

## 🔐 Environment Variables

You will need:

```bash
SLACK_BOT_TOKEN=
SLACK_SIGNING_SECRET=
AWS_REGION=
```

Store sensitive values securely (e.g., AWS Secrets Manager, Kubernetes secrets, or environment variables).

---

## 🐳 Running with Docker

Build image:

```bash
docker build -t slack-chatbot .
```

Run container:

```bash
docker run -p 8080:8080 \
  -e SLACK_BOT_TOKEN=xxx \
  -e SLACK_SIGNING_SECRET=xxx \
  slack-chatbot
```

---

## ☸ Kubernetes Deployment

Apply manifests:

```bash
kubectl apply -f KubernetesPods.yaml
```

For ARM64 clusters:

```bash
kubectl apply -f KubernetesPodsArm64.yaml
```

Ensure secrets are configured prior to deployment.

---

## ☁ Infrastructure Deployment (CDK)

Navigate to CDK directory:

```bash
cd cdk
```

Install dependencies:

```bash
npm install
```

Bootstrap (first time only):

```bash
cdk bootstrap
```

Deploy:

```bash
cdk deploy
```

---

## 🔄 CI/CD

This project includes:

- `Jenkinsfile` for automated builds
- Docker-based pipeline
- Multi-architecture support
- Version bump configuration (`.bumpversion.cfg`)

---

## 🧪 Testing

If tests are included under `lib/` or `lambdas/`, run:

```bash
pytest
```

---

## 📄 Makefile Commands

Common commands:

```bash
make build
make test
make lint
make deploy
```

Check `Makefile` for the complete list.

---

## 📚 Documentation

- `GETTINGSTARTED.md` – Initial setup guide
- `CONTRIBUTING.md` – Contribution workflow
- `CHANGELOG.md` – Release history

---

## 🔒 Security Best Practices

- Never commit Slack tokens.
- Use secret scanning tools.
- Rotate credentials if exposed.
- Validate Slack request signatures.

---

## 🏗 Architecture Overview

Slack → HTTP Endpoint → Bot Logic (lib/) → External Services

Deployment targets:

- Docker
- Kubernetes
- AWS (via CDK)
- CI/CD pipeline

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Add tests
4. Run lint + tests
5. Submit pull request

---
