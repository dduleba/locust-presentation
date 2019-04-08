import os
import sys

from locust.main import main


if __name__ == '__main__':
    sys.argv.extend(
        [
            '-f',

            os.path.join(os.path.dirname(__file__), 'locustfile_own_client.py'),

            # run parameters
            # '--no-web',
            # '--clients=20',
            # '--hatch=20'
            # '--print-stats'
            # '--help'
        ]
    )
    print(sys.argv)
    main()
