#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess,optparse,os
def p(out):
	if out:
		print out

def main():
	#Sets the default name for git to use when you commit
	user = 'Kanst'
	user_up = 'git config --global user.name "' + user + '"'
	u = subprocess.Popen(user_up, shell=True, stdout=subprocess.PIPE)
	out = u.stdout.read()
	p(out)
	Sets the default email for git to use when you commit
	mail = 'ae_jeka@mail.ru'
	mail_up = 'git config --global user.email "' + mail + '"'
	m = subprocess.Popen(mail_up, shell=True, stdout=subprocess.PIPE)
	out = m.stdout.read()
	p(out)
	# Set git to use the credential memory cache
	cache = 'git config --global credential.helper cache'
	c = subprocess.Popen(cache, shell=True, stdout=subprocess.PIPE)
	out = c.stdout.read()
	p(out)


	

	print "Если в следующем списке есть пакет xclip,\nто следует выполнить команду 'xclip -sel clip < ~/.ssh/id_rsa.pub'. После выполнения в буфере окажется публичный ключ. Иначе вначале нужно установить этот пакет (sudo apt-get install xclip)"
	print "Далее следует проверить ключи (ssh -T git@github.com). Если вылетает ошибка, то можно выполнить 'ssh-add ~/.ssh/id_rsa'"





if __name__ == '__main__':
	main()