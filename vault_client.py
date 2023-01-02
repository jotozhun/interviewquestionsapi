import hvac

client = hvac.Client(
    url="https://localhost:8200",
    token="hvs.FuOdky4g7C1yzx4ZQUPbnjn0"
)

print(client.is_authenticated())