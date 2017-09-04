#!/usr/bin/env python3
import voting


if __name__ == '__main__':
    voting.db.create_all()
    voting.app.run(port=5000, host='0.0.0.0')

