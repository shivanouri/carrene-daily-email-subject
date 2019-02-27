# Carrene Daily Report Subject Generator

As lazy a girl can be, I decided to have my daily report email subject be dailysubjectd by a routine command.
Hope other Carrene members enjoy it as I do.


## Easy Integration
### Installation
```
sudo pip3.6 install git+https://github.com/shivanouri/carrene-daily-email-subject#egg=carrene-daily-email-subject
```
### Usage
Just type the command and your Team Name at the end
```
dailysubject generate --team TeamName
```
Or easier:
```
dailysubject generate -t TeamName
```
Output (**the output gets copied to your clipboard, so you won't have to copy it yourself**):
```
Daily Report Thursday 1397/12/02 (TeamName)
```
**Team name is optional, so you can just have:**
```
dailysubject generate
```
Output:
```
Daily Report Wednesday 1397/12/08
```
