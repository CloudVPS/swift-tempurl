swift-tempurl
=============

A clone of tempurl, with support for hashes based on domainremap. Includes all features from grizzly, backported to folsom.

Rationale
---

A typical Swift URL looks like `/v1/AUTH_account/container/object`. Domainremap allows users to move 
the AUTH_account part to before the hostname of the object store. tempurl's hashing, however, still 
requires the '/v1/AUTH_' to be present.

This middleware allows hashes to be based on the following urls: `/account/container/object` and `/container/object`. Coincidently, this matches the primary paths of the CloudVPS object stores.

Concerns
---
Because three different URLS are supported for hashing, this patch reduces the strength of the hashing by 1.5 bits. Given that sha1 provides 160 bits of hash strength, this loss in strength is less than 1%, which we deem acceptable.

