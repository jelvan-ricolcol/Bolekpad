import 'package:flutter/material.dart';
import '../../theme/bolek_colors.dart';

class RightAIPanel extends StatelessWidget {
  const RightAIPanel({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 300,
      decoration: BoxDecoration(
        color: BolekColors.surface,
        border: Border(left: BorderSide(color: Colors.grey.shade300)),
      ),
      child: Column(
        children: [
          Container(
            padding: const EdgeInsets.all(16),
            color: BolekColors.primary,
            width: double.infinity,
            child: const Text('Bolek AI Assistant', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
          ),
          Expanded(
            child: ListView(
              padding: const EdgeInsets.all(16),
              children: [
                _buildActionCard(context, 'Rewrite', Icons.edit),
                _buildActionCard(context, 'Summarize', Icons.summarize),
                _buildActionCard(context, 'Grammar', Icons.spellcheck),
                _buildActionCard(context, 'Translate', Icons.translate),
                _buildActionCard(context, 'Document QA', Icons.question_answer),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: TextField(
              decoration: InputDecoration(
                hintText: 'Ask AI...',
                suffixIcon: const Icon(Icons.send, color: BolekColors.primary),
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(8)),
              ),
            ),
          )
        ],
      ),
    );
  }

  Widget _buildActionCard(BuildContext context, String title, IconData icon) {
    return Card(
      elevation: 0,
      color: BolekColors.background,
      margin: const EdgeInsets.only(bottom: 8),
      child: ListTile(
        leading: Icon(icon, color: BolekColors.primary),
        title: Text(title),
        onTap: () {
          // Trigger AI action via WebSocket
        },
      ),
    );
  }
}
