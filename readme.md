# Overwatch Network/System Monitoring Solution
Created by mlatham - Apart of CAMM IT Consulting

v1.0

Simple network monitoring solution designed to be lightweight to run on 1 core, 1 GB RAM. 

The current state of this application is NOT meant to be ran in any production environment. Project listed on Github simply for change tracking.

# v1.x Roadmap

### Alerting
- [ ] via SMTP
- [ ] via Webhook (for MS Teams)

### HTML Front End
- [ ] Authentication
- [ ] Add hosts via GUI
- [ ] View if a host is up/down (no plan for historical data in current version)


# Setup

Create and initialize the Database - `python3 setup.py --dbcreate`

Add host - `python3 setup.py --addhost`

Run - `python3 app.py`