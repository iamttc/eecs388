#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ��f��k���D�{�������l9�60ㇵ��\�g���!�4w݁�&�aK�_����J�s�%%Wt�,�#ݛ��Rl�����"����E�M�~��8&Ϊ�����(�v�S~�d�^-[
"""
from hashlib import sha256
if sha256(blob).hexdigest()[0] == 'e':
    print 'I come in peace.'
else:
    print 'Prepare to be destroyed!'
