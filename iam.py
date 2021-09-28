import iamFunctions as iam

# Create user with console access and add to new group
new_group = iam.create_group("user1")
new_user = iam.create_user("support")
iam.add_user_to_group(new_user["UserName"], new_group["GroupName"])
iam.attach_policy_to_group(new_group["GroupName"], "arn:aws:iam::aws:policy/PowerUserAccess")

# Create user with console access and add to existing group
new_user = iam.create_user("user1")
iam.add_user_to_group(new_user["UserName"], "support")
iam.attach_policy_to_group(new_group["GroupName"], "arn:aws:iam::aws:policy/PowerUserAccess")

# Create a new policy
policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "NotAction": [
                "iam:*",
                "organizations:*",
                "account:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:CreateServiceLinkedRole",
                "iam:DeleteServiceLinkedRole",
                "iam:ListRoles",
                "organizations:DescribeOrganization",
                "account:ListRegions"
            ],
            "Resource": "*"
        }
    ]
}
json_policy = json.dumps(policy, indent = 4) 
iam.create_policy("example", json_policy, description="Example policy")