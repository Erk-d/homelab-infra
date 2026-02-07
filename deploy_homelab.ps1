
$Server = "192.168.68.75"
$User = "floki"
$RemotePath = "homelab-infra/docker/"

# Check connectivity
Write-Host "Checking connectivity to $Server..."
$ping = Test-Connection -ComputerName $Server -Count 1 -Quiet
if (-not $ping) {
    Write-Error "Cannot reach $Server. Is it online?"
    exit
}

Write-Host "Deploying docker-compose.yml to $Server..."
# Copy the file
scp .\docker\docker-compose.yml "${User}@${Server}:${RemotePath}"

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed tocopy file. Check your password or path."
    exit
}

Write-Host "Updating containers on $Server..."
# Run the update
ssh "${User}@${Server}" "cd ${RemotePath} && docker-compose pull && docker-compose up -d"

if ($LASTEXITCODE -eq 0) {
    Write-Host "Deployment Complete! You can now access BookStack at http://${Server}:6875" -ForegroundColor Green
} else {
    Write-Error "Deployment failed during remote execution."
}
