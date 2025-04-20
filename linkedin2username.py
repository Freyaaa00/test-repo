import requests

def generate_usernames(company):
    # 定义一些常见的用户名格式
    formats = [
        "{first}.{last}",
        "{first}{last}",
        "{firstinitial}.{last}",
        "{firstinitial}{last}",
        "{first}.{last}@{company}.com",
        "{first}{last}@{company}.com",
        "{firstinitial}.{last}@{company}.com",
        "{firstinitial}{last}@{company}.com"
    ]
    
    # 获取公司名称的常见人名（这部分通常需要通过 LinkedIn 或其他方法获取）
    # 假设获取到的常见姓名列表（你可以使用爬虫或 LinkedIn API 获取真实数据）
    first_names = ["John", "Jane", "James", "Mary"]
    last_names = ["Doe", "Smith", "Johnson", "Williams"]
    
    # 生成用户名组合
    usernames = []
    for first in first_names:
        for last in last_names:
            for format in formats:
                # 根据格式生成用户名
                username = format.format(first=first, last=last, firstinitial=first[0], company=company.lower())
                usernames.append(username)
    
    return usernames


def main():
    # 获取用户输入的公司名称
    company = input("Enter the company name: ").strip()
    
    # 调用函数生成潜在的用户名
    usernames = generate_usernames(company)
    
    # 打印生成的用户名列表
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)

if __name__ == "__main__":
    main()
