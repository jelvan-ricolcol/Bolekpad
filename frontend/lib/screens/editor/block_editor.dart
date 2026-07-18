import 'package:flutter/material.dart';
import '../../theme/bolek_colors.dart';

class BlockEditor extends StatelessWidget {
  const BlockEditor({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text('Document Title', style: Theme.of(context).textTheme.headlineLarge),
        ),
        Expanded(
          child: ListView.builder(
            itemCount: 10, // Mock blocks
            itemBuilder: (context, index) {
              return const TextBlockWidget();
            },
          ),
        ),
      ],
    );
  }
}

class TextBlockWidget extends StatelessWidget {
  const TextBlockWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
      child: TextField(
        decoration: const InputDecoration(
          border: InputBorder.none,
          hintText: 'Type / for commands',
        ),
        style: Theme.of(context).textTheme.bodyLarge,
        maxLines: null,
      ),
    );
  }
}
