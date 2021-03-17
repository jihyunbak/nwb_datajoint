# Edit and then run this script after activating the nwb_datajoint environment
# and a mysql login has been created for you

import datajoint as dj

dj.config['database.host'] = "lmf-db.cin.ucsf.edu"

# to prevent connection error for pymysql>=0.10; may omit in future
dj.config['database.use_tls'] = False

# replace with your user name
dj.config['database.user'] = "jhbak"

# change your password
# note: changed password directly by doing `set password=PASSWORD('avocado');`
#dj.set_password()

# replace "password_here" with the password that you used in the dj.set_password() above
dj.config['database.password'] = "avocado"

dj.config.save_global()
