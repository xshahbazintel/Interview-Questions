register module saves output of the execute task
eg: 
    - name: Check if httpd service is active
      ansible.builtin.systemd:
        name: httpd
        state: started
      register: httpd_status
      ignore_errors: yes

debug prints message on the console
- name: Display httpd service status
      debug:
        msg: "httpd service is running"
      when: httpd_status.state == "started"

What are Ansible tasks?
The task is a unit action of Ansible. It helps by breaking a configuration policy into smaller files or blocks of code. These blocks can be used in automating a process. For example, to install a package or update a software

what are ansible handlers?
Handlers are like special tasks which only run if the Task contains a “notify” directive. 
tasks:
  - name: install nginx
    apt: pkg=nginx state=installed update_cache=true
    notify:
     - start nginx
 handlers:
   - name: start nginx
     service: name=nginx state=started

What is Ansible Vault?
Ansible vault is used to keep sensitive data such as passwords instead of placing it as plaintext in playbooks or roles. 
Any structured data file or any single value inside the YAML file can be encrypted by Ansible. 


