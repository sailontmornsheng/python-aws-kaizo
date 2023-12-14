# AWS EC2 Instance Fetcher

This Python script uses Boto3 to fetch information about running EC2 instances on AWS. It prompts the user for their AWS credentials and region, then retrieves details about running instances, including instance ID, state, public IP, and private IP.

## Prerequisites

- Python 3.x installed



## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/sailontmornsheng/python-aws-kaizo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd aws-ec2-instance-fetcher
    ```

3. Install Required Packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Install Required Packages:

    ```bash
    python ec2_instance_fetcher.py
    ```

5. Enter your AWS Access Key, AWS Secret Key, and AWS Region as prompted.

6. The script will fetch information about running EC2 instances and export it to an Excel file with a name like `running_instances_<region>.xlsx`.

## Note

- Ensure that your AWS credentials have the necessary permissions to describe EC2 instances.

- The script stores credentials in memory and doesn't persist them. For production use, consider using AWS Identity and Access Management (IAM) roles.

<br>
<br>

_______________

# EC2 Instances Information Retrieval Script

This Python script interacts with the AWS CLI and the `boto3` library to fetch information about EC2 instances. The script prompts the user for AWS credentials or profile, the AWS region to fetch EC2 instances, and the desired output format (Excel or JSON). The retrieved data includes details such as instance name, instance ID, state, instance type, region, security groups, and associated key pairs.

## Prerequisites

- Python 3
- AWS CLI installed and configured with necessary credentials (if not using a profile)

## Installation

1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the script:

    ```bash
    python aws-ec2-instance-fetcher-2.py
    ```

## Usage

Follow the prompts to provide AWS credentials, choose an AWS profile, select the AWS region, and specify the desired output format. The script will fetch and display information about EC2 instances based on your inputs.

## Output

The script exports the retrieved data in either Excel or JSON format, naming the output files based on the specified AWS region and the current date.

- Excel Output: `ec2_instances_region_date.xlsx`
- JSON Output: `ec2_instances_region_date.json`

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
