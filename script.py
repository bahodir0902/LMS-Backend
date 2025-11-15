# Run this script to set the bucket policy programmatically
# Install: pip install minio

import json

from minio import Minio


def set_public_bucket_policy():
    # Initialize MinIO client with your credentials
    client = Minio(
        "127.0.0.1:9000",
        access_key="minio",  # or "minioadmin" if using your current setup
        secret_key="minio123",  # or "minioadmin" if using your current setup
        secure=False,
    )

    bucket_name = "media"

    # Define public read policy
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": ["s3:GetObject"],
                "Resource": [f"arn:aws:s3:::{bucket_name}/*"],
            }
        ],
    }

    try:
        # Set the bucket policy
        client.set_bucket_policy(bucket_name, json.dumps(policy))
        print(f"✅ Public read policy set successfully for bucket '{bucket_name}'")

        # Verify the policy
        current_policy = client.get_bucket_policy(bucket_name)
        print(f"✅ Current policy: {current_policy}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    set_public_bucket_policy()
