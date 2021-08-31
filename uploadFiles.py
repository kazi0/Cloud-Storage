import dropbox
import os


class TransferData:
    def __init__(self, access_token):
        self.aT = access_token

    def upload_file(self, file_from):
        db = dropbox.Dropbox(self.aT)
        fileName = os.path.split(
            file_from)[1]

        dropbox_file = '/CloudStorage/'+fileName

        with open(file_from, "rb") as f:
            db.files_upload(f.read(), dropbox_file,
                            mode=dropbox.files.WriteMode.overwrite)


AToken = "sl.A3kcE1hq21bA1cHmoGDzuDWet8IfrK-lFsSkw6miOaT4VCSONb_dyy66ab9rzRn7PnxnM-W-jvc4RadqOE3TEcs_mOqMW6brlQGd64WXRdtn5F0oBxStFdTly_l9mpzHNDXfQ6M"

cloudStoring = TransferData(AToken)

fileFrom = input("Please Give the File Path To Transfer ")

while(os.path.isfile(fileFrom) == False):
    print("Pls Give The Path Of A File")
    fileFrom = input("Please Give the File Path To Transfer ")

cloudStoring.upload_file(fileFrom)

print("Files Have Been Stored On Dropbox ;)")