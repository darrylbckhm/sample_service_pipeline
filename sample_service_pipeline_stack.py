from aws_cdk import core

from .cluster import Cluster
from .pipeline import SampleServicePipeline
from .webapp import WebApp


class SampleServicePipelineStack(core.Stack):
    """
    A stack for deploying up a dockerized Django application
    in ECS through Fargate with a full CICD pipeline.
    """

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cluster = Cluster(self, 'Cluster')
        webapp = WebApp(self, 'WebApp', cluster=cluster)
        pipeline = SampleServicePipeline(self, 'Pipeline', webapp=webapp)
