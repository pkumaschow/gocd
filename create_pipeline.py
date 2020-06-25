#!venv/bin/python

from gomatic import *

print('\033[32m' + 'Injecting a pipeline into GoCD' + '\033[0m')  # Red text

#configurator = GoCdConfigurator(HostRestClient("localhost:8153", ssl=False, username='admin', password='abc123'))
configurator = GoCdConfigurator(HostRestClient("localhost:8153", ssl=False))
pipeline = configurator\
	.ensure_pipeline_group("group1")\
	.ensure_replacement_of_pipeline("P12")\
	.set_git_material(GitMaterial("https://github.com/pkumaschow/gocd.git", material_name="mx"))
stage = pipeline.ensure_stage("S1")
job = stage.ensure_job("J1")
job.add_task(ExecTask(['ls']))

configurator.save_updated_config(save_config_locally=True, dry_run=False)
