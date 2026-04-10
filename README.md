# Automated Infrastructure Audit Tool

## Project Overview
This tool was developed to automate hardware verification and system health monitoring for high-performance computer laboratories. It was specifically utilized during the deployment of a 15-node GPU-powered lab at Quaid-e-Azam Grammar School.

## Key Features
- **Hardware Detection:** Identifies CPU, RAM, and Disk specifications.
- **GPU Compliance:** Verifies the presence of dedicated NVIDIA/GTX hardware for heavy workloads.
- **Automated Reporting:** Provides a status update on whether the hardware meets pre-defined lab requirements.

## Tech Stack
- **Language:** Python 3.x
- **Libraries:** psutil, platform, subprocess
