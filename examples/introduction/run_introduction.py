import os
import sys

from locust.main import main


if __name__ == '__main__':
    sys.argv.extend(
        [
            '-f',
            # Hello world example

            os.path.join(os.path.dirname(__file__), 'locustfile_hello_world.py'),

            # Weight example

            # os.path.join(os.path.dirname(__file__), 'locustfile_weight.py'),
            # 'MobileUserLocust',

            # run parameters
            '--no-web',
            '--clients=20',
            '--hatch=20'
            # '--print-stats'
            # '--help'
        ]
    )
    # sys.argv.extend(example_01_args())
    print(sys.argv)
    main()
