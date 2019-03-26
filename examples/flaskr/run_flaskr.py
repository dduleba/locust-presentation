import os
import sys

from locust.main import main


if __name__ == '__main__':
    sys.argv.extend(
        [
            '-f',
            # Hello world example

            # os.path.join(os.path.dirname(__file__), 'locustfile_index.py'),
            # os.path.join(os.path.dirname(__file__), 'locustfile_register.py'),
            os.path.join(os.path.dirname(__file__), 'locustfile_logged.py'),

            # Weight example

            # os.path.join(os.path.dirname(__file__), 'locustfile_weight.py'),
            # 'MobileUserLocust',

            # run parameters
            '--print-stats',
            # '--no-web',
            # '--clients=2',
            # '--hatch=10'
            # '--help'

            # '--host', 'http://127.0.0.1:5001'
        ]
    )
    # sys.argv.extend(example_01_args())
    print(sys.argv)
    main()
