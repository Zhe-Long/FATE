#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0

#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

from .components import ComponentMeta

"""
define components
"""
dataio_cpn_meta = ComponentMeta("DataIO")


@dataio_cpn_meta.bind_param
def dataio_param():
    from federatedml.param.dataio_param import DataIOParam

    return DataIOParam


@dataio_cpn_meta.bind_runner.on_guest.on_host
def dataio_runner():
    from federatedml.util.data_io import DataIO

    return DataIO


hetero_binning_cpn_meta = ComponentMeta("HeteroFeatureBinning")


@hetero_binning_cpn_meta.bind_param
def hetero_feature_binning_param():
    from federatedml.param.feature_binning_param import HeteroFeatureBinningParam

    return HeteroFeatureBinningParam


@hetero_binning_cpn_meta.bind_runner.on_guest
def hetero_feature_binning_guest_runner():
    from federatedml.feature.hetero_feature_binning.hetero_binning_guest import (
        HeteroFeatureBinningGuest,
    )

    return HeteroFeatureBinningGuest


@hetero_binning_cpn_meta.bind_runner.on_host
def hetero_feature_binning_host_runner():
    from federatedml.feature.hetero_feature_binning.hetero_binning_host import (
        HeteroFeatureBinningHost,
    )

    return HeteroFeatureBinningHost


hetero_feature_selection_cpn_meta = ComponentMeta("HeteroFeatureSelection")


@hetero_feature_selection_cpn_meta.bind_param
def hetero_feature_selection_param():
    from federatedml.param.feature_selection_param import FeatureSelectionParam

    return FeatureSelectionParam


@hetero_feature_selection_cpn_meta.bind_runner.on_guest
def hetero_feature_selection_guest_runner():
    from federatedml.feature.hetero_feature_selection.feature_selection_guest import (
        HeteroFeatureSelectionGuest,
    )

    return HeteroFeatureSelectionGuest


@hetero_feature_selection_cpn_meta.bind_runner.on_host
def hetero_feature_selection_host_runner():
    from federatedml.feature.hetero_feature_selection.feature_selection_host import (
        HeteroFeatureSelectionHost,
    )

    return HeteroFeatureSelectionHost


intersection_cpn_meta = ComponentMeta("Intersection")


@intersection_cpn_meta.bind_param
def intersection_param():
    from federatedml.param.intersect_param import IntersectParam

    return IntersectParam


@intersection_cpn_meta.bind_runner.on_guest
def intersection_guest_runner():
    from federatedml.statistic.intersect.intersect_model import IntersectGuest

    return IntersectGuest


@intersection_cpn_meta.bind_runner.on_host
def intersection_host_runner():
    from federatedml.statistic.intersect.intersect_model import IntersectHost

    return IntersectHost


hetero_lr_cpn_meta = ComponentMeta("HeteroLR")


@hetero_lr_cpn_meta.bind_param
def hetero_lr_param():
    from federatedml.param.logistic_regression_param import HeteroLogisticParam

    return HeteroLogisticParam


@hetero_lr_cpn_meta.bind_runner.on_guest
def hetero_lr_runner_guest():
    from federatedml.linear_model.logistic_regression.hetero_logistic_regression.hetero_lr_guest import (
        HeteroLRGuest,
    )

    return HeteroLRGuest


@hetero_lr_cpn_meta.bind_runner.on_host
def hetero_lr_runner_host():
    from federatedml.linear_model.logistic_regression.hetero_logistic_regression.hetero_lr_host import (
        HeteroLRHost,
    )

    return HeteroLRHost


@hetero_lr_cpn_meta.bind_runner.on_arbiter
def hetero_lr_runner_arbiter():
    from federatedml.linear_model.logistic_regression.hetero_logistic_regression.hetero_lr_arbiter import (
        HeteroLRArbiter,
    )

    return HeteroLRArbiter


evaluation_cpn_meta = ComponentMeta("Evaluation")


@evaluation_cpn_meta.bind_param
def evaluation_param():
    from federatedml.param.evaluation_param import EvaluateParam

    return EvaluateParam


@evaluation_cpn_meta.bind_runner.on_guest.on_host.on_arbiter
def evaluation_runner():
    from federatedml.evaluation.evaluation import Evaluation

    return Evaluation