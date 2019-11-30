# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
	config.vm.box = "bento/ubuntu-18.10"
    config.ssh.forward_agent = false
    config.vm.provider "virtualbox" do |v|
        v.memory = 1024
    end

    config.vm.define "dwpapi", primary: true do |dwpapi|
        dwpapi.vm.hostname = "dwpapi"
        dwpapi.vm.network "forwarded_port", guest: 5000, host: 5000

        config.vm.synced_folder "../", "/opt/dev"

        dwpapi.vm.provision "ansible_local" do |a|
            a.verbose = "v"
            a.playbook = "setup_dwpapi.yml"
        end
    end
end