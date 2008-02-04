import re

def validate_expression(value, expression, **kwargs):
    ignore = kwargs.get('ignore', None)
    if ignore:
        if isinstance(ignore, basestring):
            ignore = re.compile(ignore)
        value = ignore.sub('', value)
    if expression.match(value):
        return True
    return False
    
def isSSN(value, **kwargs):
    expr = re.compile(r'^\d{9}$')
    errmsg = 'is not a well formed SSN.'
    return validate_expression(value, expr, errmsg=errmsg, **kwargs)

def isUSPhoneNumber(value, **kwargs):
    expr = re.compile(r'^\d{10}$')
    if not kwargs.get('ignore', None):
        kwargs['ignore'] = re.compile(r'[\(\)\-\s]')
    errmsg = 'is not a valid us phone number.'
    return validate_expression(value, expr, errmsg=errmsg, **kwargs)
    
def isInternationalPhoneNumber(value, **kwargs):
    expr = re.compile(r'^\d+$')
    if not kwargs.get('ignore', None):
        kwargs['ignore'] = re.compile(r'[\(\)\-\s\+]')
    errmsg = 'is not a valid international phone number.'
    return validate_expression(value, expr, errmsg=errmsg, **kwargs)
    
def isZipCode(value, **kwargs):
    expr = re.compile(r'^(\d{5}|\d{9})$')
    errmsg = 'is not a valid zip code.'
    return validate_expression(value, expr, errmsg=errmsg, **kwargs)
    
def isURL(value, **kwargs):
    protocols = ('http', 'ftp', 'irc', 'news', 'imap', 'gopher', 'jabber',
        'webdav', 'smb', 'fish', 'ldap', 'pop3', 'smtp', 'sftp', 'ssh'
    )
    expr = re.compile(r'(%s)s?://[^\s\r\n]+' % '|'.join(protocols))
    errmsg = 'is not a valid url.'
    return validate_expression(value, expr, errmsg=errmsg, **kwargs)
    
def isEmail(value, **kwargs):
    expr = re.compile(r"^(\w&.%#$&'\*+-/=?^_`{}|~]+!)*[\w&.%#$&'\*+-/=?^_`{}|~]+@(([0-9a-z]([0-9a-z-]*[0-9a-z])?\.)+[a-z]{2,6}|([0-9]{1,3}\.){3}[0-9]{1,3})$", re.IGNORECASE)
    errmsg = 'is not a valid email address.'
    return validate_expression(value, expr, errmsg=errmsg, **kwargs)