# btmx-demo

Demonstrates how to use betamax to record and replay API responses during
tests. Recorded responses are saved to `btmx-demo/test/cassettes`. It would
make sense to delete these and re-record responses periodically.

Once responses have been recorded the tests can be run without hitting the
remote API.

# Setup

    python bootstrap.py
    ./bin/buildout


# Test

    ./bin/py.test btmx-demo/test
