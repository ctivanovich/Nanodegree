#!/bin/bash
aws ec2 disassociate-address --association-id eipassoc-5fee7c60
aws ec2 release-address --allocation-id eipalloc-4e86e773
aws ec2 terminate-instances --instance-ids i-0532431a82b095705
aws ec2 wait instance-terminated --instance-ids i-0532431a82b095705
aws ec2 delete-security-group --group-id sg-8b144bf6
aws ec2 disassociate-route-table --association-id rtbassoc-f618108e
aws ec2 delete-route-table --route-table-id rtb-19f49360
aws ec2 detach-internet-gateway --internet-gateway-id igw-ff9ea198 --vpc-id vpc-9c527cfa
aws ec2 delete-internet-gateway --internet-gateway-id igw-ff9ea198
aws ec2 delete-subnet --subnet-id subnet-9b70e0d3
aws ec2 delete-vpc --vpc-id vpc-9c527cfa
echo If you want to delete the key-pair, please do it manually.
