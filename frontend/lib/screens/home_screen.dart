import 'package:flutter/material.dart';
import 'editor/block_editor.dart';
import 'ai/right_ai_panel.dart';
import '../theme/bolek_colors.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Bolek Docs', style: TextStyle(color: Colors.white)),
        backgroundColor: BolekColors.primary,
        elevation: 1,
      ),
      body: const Row(
        children: [
          Expanded(child: BlockEditor()),
          RightAIPanel(),
        ],
      ),
    );
  }
}

