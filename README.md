## Description

Tasks is a tool that will recursivley search a directory of scheduled task XML files and process the data within into an output CSV file. 

Run this as administrator for best results. If the task file is still not accessible, you can use a tool like `carve.py` to collect the files first before processing. 

Because this program collect ALL of the information from the tasks, you may want to post-process this file to narrow down to relevant information, such as task name, context, exection commands and arguments, etc. 

## Installation

The easiest way to install the dependencies is with:

    pip install -r requirements.txt

## Syntax
    usage: tasks.py [-h] [-t TASKS] -o OUTPUT

    Tasks is a tool that will recursivley search a directory of scheduled task XML files and process the data within into an output CSV file.

    options:
    -h, --help            show this help message and exit
    -t TASKS, --tasks TASKS
                            Path to the root of the tasks folder. Default is the local system tasks folder. (default: C:\windows\system32\tasks\)
    -o OUTPUT, --output OUTPUT
                            Output csv file. (default: None)

    v1.0.0 | Author: Stephen Hurd | @HurdDFIR

## Examples
Simple usage:

    python3 .\tasks.py -o tasks.csv

Simple usage with custom directory to search:

    python3 .\tasks.py -t 'D:\case_number\hostname\triage_collection\C\Windows\System32\Tasks\' -o tasks.csv

## Disclaimer

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## License

MIT
