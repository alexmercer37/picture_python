"""


"""
import argparse
import onnx_graphsurgeon as gs
import onnx
import numpy as np
from onnx import version_converter, helper



def bst_cut_yolov5(nodes,weights):
    model_path = weights
    user_nodes = nodes

    assert model_path[-5:] =='.onnx', f"required onnx file not {model_path}"

    user_nodes = user_nodes.split(",")
    #user_nodes =["/model.24/m.0/Conv","/model.24/m.1/Conv","/model.24/m.2/Conv"]

    print(user_nodes)
    # assert len(user_nodes) == 3, "Pleaase enter 3 nodes and using ',' to split them"
    user_nodes={i:'0' for i in user_nodes}

    #load graph & nodes
    graph_backbone = gs.import_onnx(onnx.load(model_path))
    graph_head = gs.import_onnx(onnx.load(model_path))

    backbone_nodes = graph_backbone.nodes
    backbone_nodes = {i.name:i for i in backbone_nodes}

    head_nodes = graph_head.nodes
    head_nodes = {i.name:i for i in head_nodes}

    backbone_outputs = []
    head_inputs = []
    new_map = {}

    #check nodes and cut&build graph
    for index,node in enumerate(list(user_nodes.keys())):
        assert node in backbone_nodes , f"{node} not found in your model, please double check it"
        backbone_nodes_output = backbone_nodes[node].outputs
        assert len(backbone_nodes_output)==1, f" your node {node} have multi outputs, it should have only one"

        head_node_name =backbone_nodes_output[0].outputs[0].name
        inter_tensor_name = backbone_nodes_output[0].name
        # shape = tuple(backbone_nodes_output[0].shape)
        shape = backbone_nodes_output[0].shape

        user_nodes[node] = "output_"+str(index)
        user_nodes[head_node_name] = "input_"+str(index)
        new_map["output_"+str(index)] = "input_"+str(index)

        backbone_output = gs.Variable(name=user_nodes[node],dtype=np.float32, shape=shape)
        head_input = gs.Variable(name=user_nodes[head_node_name],dtype=np.float32, shape=shape)

        # assert len(head_nodes[head_node_name].inputs)==1, f" your node {node} have multi inputs, it should have only one"
        
        input_tensor_index = None
        for index, input_node in enumerate(head_nodes[head_node_name].inputs):
            if input_node.name == inter_tensor_name:
                input_tensor_index = index
                break
        head_nodes[head_node_name].inputs[input_tensor_index] = head_input
        head_nodes[node].outputs.clear()
        head_inputs.append(head_input)


        backbone_nodes[node].outputs = [backbone_output]
        backbone_nodes[head_node_name].inputs.clear()
        backbone_outputs.append(backbone_output)




    graph_backbone.outputs=backbone_outputs
    graph_head.inputs = head_inputs

    graph_backbone.cleanup().toposort()
    graph_head.cleanup().toposort()


    onnx_model_backbone = gs.export_onnx(graph_backbone,do_type_check=True)
    onnx_model_heade = gs.export_onnx(graph_head,do_type_check=True)

    onnx_model_backbone.ir_version = 6
    onnx_model_backbone = version_converter.convert_version(onnx_model_backbone,13)#13
    onnx_model_backbone.opset_import[0].version = 13
    onnx.checker.check_model(onnx_model_backbone)
    onnx.save(onnx_model_backbone, model_path[:-5]+'_backbone.onnx')

    onnx_model_heade.ir_version = 6
    onnx_model_heade = version_converter.convert_version(onnx_model_heade,13)
    onnx_model_heade.opset_import[0].version = 13
    onnx.checker.check_model(onnx_model_heade)
    onnx.save(onnx_model_heade, model_path[:-5]+'_head.onnx')   

    print("your node map is ")
    print(user_nodes)

    print("your new map is ")
    print(new_map)


def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--nodes', type=str, required=True, help='your cut nodes, should split by , ')
    parser.add_argument('--weights',type=str, required=True, help='onnx weights path')
    opt = parser.parse_args()
    print(vars(opt))
    return opt


if __name__ == "__main__":
    opt = parse_opt()
    bst_cut_yolov5(**vars(opt))
