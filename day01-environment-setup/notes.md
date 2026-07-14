Microsoft Windows [Version 10.0.26200.8655]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Student>ssh dgx-s-pu-soe-20241cai0163@172.19.0.11
dgx-s-pu-soe-20241cai0163@172.19.0.11's password:
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-51-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

Expanded Security Maintenance for Applications is not enabled.

439 updates can be applied immediately.
216 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

2 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Welcome to Base Command Manager 11.0

                                            Based on Ubuntu Noble Numbat 24.04
                                                    Cluster Manager ID: #00000

Use the following commands to adjust your environment:

'module avail'            - show available modules
'module add <module>'     - adds a module to your environment for this session
'module initadd <module>' - configure module to be loaded at every login
                            (Note: initadd is available only for Tcl modules)

-------------------------------------------------------------------------------
Last login: Tue Jul 14 08:37:48 2026 from 172.19.3.140
Loading gcc/14.2.0
  Loading requirement: gmp/6.3.0 mpfr/4.2.1 mpc/1.3.1
dgx-s-pu-soe-20241cai0163@presidency-headnode:~$ vim pod.yaml
dgx-s-pu-soe-20241cai0163@presidency-headnode:~$ kubectl apply -f pod.yaml
pod/my-pod-1 created
service/my-service-1 unchanged
dgx-s-pu-soe-20241cai0163@presidency-headnode:~$ kubectl get pod,service
NAME           READY   STATUS    RESTARTS   AGE
pod/my-pod-1   1/1     Running   0          19s

NAME                   TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/my-service-1   NodePort   10.150.130.113   <none>        8000:31940/TCP   18m
dgx-s-pu-soe-20241cai0163@presidency-headnode:~$ kubectl exec -it my-pod-1 -- bash
root@my-pod-1:/workspace# jupyter lab --NotebookApp.token='1234'
[I 2026-07-14 03:31:41.064 ServerApp] jupyter_lsp | extension was successfully linked.
[I 2026-07-14 03:31:41.067 ServerApp] jupyter_server_terminals | extension was successfully linked.
[W 2026-07-14 03:31:41.068 LabApp] 'token' has moved from NotebookApp to ServerApp. This config will be passed to ServerApp. Be sure to update your config before our next release.
[W 2026-07-14 03:31:41.069 ServerApp] ServerApp.token config is deprecated in 2.0. Use IdentityProvider.token.
[I 2026-07-14 03:31:41.069 ServerApp] jupyterlab | extension was successfully linked.
[I 2026-07-14 03:31:41.070 ServerApp] jupyterlab_code_formatter | extension was successfully linked.
[I 2026-07-14 03:31:41.070 ServerApp] jupyterlab_jupytext | extension was successfully linked.
[I 2026-07-14 03:31:41.070 ServerApp] jupyterlab_tensorboard_pro | extension was successfully linked.
[I 2026-07-14 03:31:41.072 ServerApp] notebook | extension was successfully linked.
[I 2026-07-14 03:31:41.073 ServerApp] Writing Jupyter server cookie secret to /root/.local/share/jupyter/runtime/jupyter_cookie_secret
[I 2026-07-14 03:31:41.198 ServerApp] notebook_shim | extension was successfully linked.
[I 2026-07-14 03:31:41.210 ServerApp] notebook_shim | extension was successfully loaded.
[I 2026-07-14 03:31:41.211 ServerApp] jupyter_lsp | extension was successfully loaded.
[I 2026-07-14 03:31:41.211 ServerApp] jupyter_server_terminals | extension was successfully loaded.
[I 2026-07-14 03:31:41.212 LabApp] JupyterLab extension loaded from /usr/local/lib/python3.10/dist-packages/jupyterlab
[I 2026-07-14 03:31:41.212 LabApp] JupyterLab application directory is /usr/local/share/jupyter/lab
[I 2026-07-14 03:31:41.213 LabApp] Extension Manager is 'pypi'.
[I 2026-07-14 03:31:41.253 ServerApp] jupyterlab | extension was successfully loaded.
[I 2026-07-14 03:31:41.253 ServerApp] Registered jupyterlab_code_formatter server extension
[I 2026-07-14 03:31:41.253 ServerApp] jupyterlab_code_formatter | extension was successfully loaded.
[I 2026-07-14 03:31:41.253 ServerApp] [Jupytext Server Extension] NotebookApp.contents_manager_class is (a subclass of) jupytext.TextFileContentsManager already - OK
[I 2026-07-14 03:31:41.253 ServerApp] jupyterlab_jupytext | extension was successfully loaded.
[I 2026-07-14 03:31:41.652 ServerApp] jupyterlab_tensorboard_pro extension loaded.
[I 2026-07-14 03:31:41.652 ServerApp] jupyterlab_tensorboard_pro | extension was successfully loaded.
[I 2026-07-14 03:31:41.654 ServerApp] notebook | extension was successfully loaded.
[I 2026-07-14 03:31:41.654 ServerApp] Serving notebooks from local directory: /workspace
[I 2026-07-14 03:31:41.654 ServerApp] Jupyter Server 2.14.2 is running at:
[I 2026-07-14 03:31:41.654 ServerApp] http://hostname:8888/lab?token=...
[I 2026-07-14 03:31:41.654 ServerApp]     http://127.0.0.1:8888/lab?token=...
[I 2026-07-14 03:31:41.654 ServerApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[I 2026-07-14 03:31:41.668 ServerApp] Skipped non-installed server(s): bash-language-server, dockerfile-language-server-nodejs, javascript-typescript-langserver, jedi-language-server, julia-language-server, pyright, python-language-server, python-lsp-server, r-languageserver, sql-language-server, texlab, typescript-language-server, unified-language-server, vscode-css-languageserver-bin, vscode-html-languageserver-bin, vscode-json-languageserver-bin, yaml-language-server
[I 2026-07-14 03:32:12.321 ServerApp] 302 GET / (@192.168.100.1) 0.42ms
[I 2026-07-14 03:32:12.326 LabApp] 302 GET /lab? (@192.168.100.1) 0.53ms
[I 2026-07-14 03:32:17.204 ServerApp] User 5a582a4ed1014df2b825f8560f64c7fc logged in.
[I 2026-07-14 03:32:17.205 ServerApp] 302 POST /login?next=%2Flab%3F (5a582a4ed1014df2b825f8560f64c7fc@192.168.100.1) 1.11ms
[W 2026-07-14 03:32:18.051 LabApp] Could not determine jupyterlab build status without nodejs
^C[I 2026-07-14 03:32:27.695 ServerApp] interrupted
[I 2026-07-14 03:32:27.696 ServerApp] Serving notebooks from local directory: /workspace
    0 active kernels
    Jupyter Server 2.14.2 is running at:
    http://hostname:8888/lab?token=...
        http://127.0.0.1:8888/lab?token=...
Shut down this Jupyter server (y/[n])? y
[C 2026-07-14 03:32:30.007 ServerApp] Shutdown confirmed
[I 2026-07-14 03:32:30.007 ServerApp] Shutting down 8 extensions
root@my-pod-1:/workspace# exit
exit
dgx-s-pu-soe-20241cai0163@presidency-headnode:~$