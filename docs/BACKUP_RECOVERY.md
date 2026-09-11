# Backup & Operational Continuity Guidelines

## 1. Version Control & Immutability
All source assets for the PEIS website are version-controlled within Git. The repository is completely self-contained and reproducible.

---

## 2. Disaster Recovery Protocol

Because the website utilizes zero proprietary state or dynamic databases, disaster recovery is instantaneous:

1. **Repository Redundancy**: Maintain mirrored private Git remotes (e.g., GitHub, GitLab, offline backup archive).
2. **Edge Provider Failover**: If primary hosting (e.g. Cloudflare Pages) encounters an outage, the site can be redeployed to GitHub Pages, Netlify, or an AWS S3 bucket within under 2 minutes by updating DNS CNAME records.
3. **Local Offline Copy**: The entire website can be served locally or from any air-gapped web server using standard static web servers (`nginx`, `caddy`, `python http.server`).
