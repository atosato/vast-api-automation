Basic automation samples for VAST Data platform
----
checkmk-vast-agent.py is a simple agent to query VAST using local check:
https://docs.checkmk.com/latest/en/localchecks.html

Create a Python virtual environment:
```
python3 -m venv venv
source venv/bin/activate
pip3 install --upgrade pip setuptools wheel
pip3 install pip-tools
pip-sync
```
If you want to update the requirements libs version:
```
pip-compile requirements.in
pip-sync
```

To use these playbooks you need to install the **VAST PythonSDK**: <link>https://github.com/vast-data/vastpy</link>.
```
pip install vastpy
```

Create a .env file with the following variables:
```
API_USERNAME = <username>
API_PASSWORD = <password>
VMS_IP = <VMS IP>
```

## How to use it
```
python3 checkmk-vast-agent.py
```



**Tested with:**
VAST release 5.2.0


----
# LICENSE
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
