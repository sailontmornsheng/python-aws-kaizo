# AWS EC2 Instance Fetcher

This Python script uses Boto3 to fetch information about running EC2 instances on AWS. It prompts the user for their AWS credentials and region, then retrieves details about running instances, including instance ID, state, public IP, and private IP.

## Prerequisites

- Python 3.x installed

Run the following command to install required packages:
```
pip install -r requirements.txt
```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/sailontmornsheng/python-aws-kaizo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd aws-ec2-instance-fetcher
    ```

3. Run the script:

    ```bash
    python ec2_instance_fetcher.py
    ```

4. Enter your AWS Access Key, AWS Secret Key, and AWS Region as prompted.

5. The script will fetch information about running EC2 instances and export it to an Excel file with a name like `running_instances_<region>.xlsx`.

## Note

- Ensure that your AWS credentials have the necessary permissions to describe EC2 instances.

- The script stores credentials in memory and doesn't persist them. For production use, consider using AWS Identity and Access Management (IAM) roles.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
