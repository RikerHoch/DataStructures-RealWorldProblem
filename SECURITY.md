# Security Policy

## Supported Versions

The Delivery Routing System is currently an academic project developed in Python 3.11. Security updates and fixes will be applied to the latest development version.

| Version | Supported |
| ------- | --------- |
| Current development version | :white_check_mark: |
| Previous versions | :x: |

Only the current development version is actively maintained. Older versions may contain unresolved issues and will not receive security updates.

## Reporting a Vulnerability

If you discover a security vulnerability or potential security issue in this project, please report it to the project maintainer through the repository's GitHub contact or private vulnerability reporting feature.

When reporting a vulnerability, please include:

- A clear description of the security issue.
- Steps to reproduce the issue.
- The potential impact on the application.
- Any relevant error messages or supporting evidence.

### Response Expectations

- Reports will be reviewed as soon as reasonably possible.
- The reporter will receive an acknowledgement when the issue has been reviewed.
- If the vulnerability is accepted, appropriate fixes will be considered and applied to the current development version.
- If the vulnerability is declined, an explanation will be provided where possible.

Please avoid publicly disclosing vulnerabilities until they have been reviewed.

## Security Considerations

This project is an educational delivery-routing simulation using Breadth-First Search (BFS), A* search, and the Observer design pattern.

The current implementation:

- Uses an in-memory weighted graph for delivery routes.
- Does not require user authentication or store personal account information.
- Does not connect to external databases or third-party services.
- Uses simulated driver and customer notifications through the Observer pattern.

The project is intended for educational demonstration and is not currently designed for production deployment or handling sensitive customer information.

Contributions and reports that help improve the security and reliability of the project are welcome.
