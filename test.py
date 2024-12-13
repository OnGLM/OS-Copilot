import os

from oscopilot import FridayAgent
from oscopilot import ToolManager
from oscopilot import FridayExecutor, FridayPlanner, FridayRetriever
from oscopilot.utils import setup_config, setup_pre_run
from zhipuai import ZhipuAI

api_key = os.getenv('OPENAI_API_KEY')
model = os.getenv('MODEL_NAME')
args = setup_config()
if not args.query:
    args.query = "将working_dir/introduce目录下包含'山东'这个词的任何文本文件复制到一个名为'shandong'的新文件夹中"
task = setup_pre_run(args)
agent = FridayAgent(FridayPlanner, FridayRetriever, FridayExecutor, ToolManager, config=args)
agent.run(task=task)

# 读取agents文件夹下的内容
agents_folder = '/home/ecs-user/OS-Copilot/working_dir/shandong'
all_files_content = ''

for filename in os.listdir(agents_folder):
    file_path = os.path.join(agents_folder, filename)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            all_files_content += file.read()

client = ZhipuAI(api_key=api_key) # 填写您自己的APIKey
response = client.chat.completions.create(
    model=model,  # 填写需要调用的模型编码
    messages=[
        {"role": "system", "content": "请帮我从下面的每个人的自我介绍中把人名列举出来，并以该格式进行回复：位于山东的同学有："},
        {"role": "user", "content": all_files_content}
    ],
)
print("************************</result>*************************")
print(response.choices[0].message)
print("************************</result>*************************")