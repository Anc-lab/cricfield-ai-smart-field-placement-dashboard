# Security Policy

## Supported Versions

Security updates are handled on the default branch until formal releases are created.

## Reporting a Vulnerability

Do not open public issues for suspected vulnerabilities, secrets, tokens, or private configuration.

Report security concerns privately to the maintainer with:

- Affected file, feature, or deployment path
- Steps to reproduce
- Potential impact
- Any suggested remediation

The maintainer will acknowledge valid reports as soon as practical and coordinate a fix before public disclosure.

## Secret Handling

- Do not commit API keys, `.env` files, Streamlit secrets, or service tokens.
- Use `.env.example` for documented variable names only.
- Rotate any credential that may have been committed, logged, pasted into an issue, or exposed in CI.
